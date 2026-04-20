(() => {
    const challengeSpan = document.getElementById('captcha-challenge');
    const answerInput = document.getElementById('arithmetic-answer');
    const refreshButton = document.getElementById('refresh-captcha');
    const errorMessage = document.getElementById('arithmetic-error');
    const attemptsMessage = document.getElementById('captcha-attempts-error');
    const canvas = document.getElementById('captcha-canvas');

    if (!challengeSpan || !answerInput || !refreshButton || !errorMessage || !attemptsMessage || !canvas) {
        return;
    }

    const context = canvas.getContext('2d');
    let expectedAnswer = 0;
    let incorrectAttempts = 0;
    const maxIncorrectAttempts = 3;

    function randomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function buildChallenge() {
        const operations = ['+', '-', '*'];
        const operation = operations[randomInt(0, operations.length - 1)];
        let num1 = randomInt(1, 15);
        let num2 = randomInt(1, 15);

        if (operation === '-') {
            if (num2 > num1) {
                const temp = num1;
                num1 = num2;
                num2 = temp;
            }
            expectedAnswer = num1 - num2;
        } else if (operation === '+') {
            expectedAnswer = num1 + num2;
        } else {
            expectedAnswer = num1 * num2;
        }

        return `${num1} ${operation} ${num2} = ?`;
    }

    function drawCaptchaImage(text) {
        if (!context) {
            return;
        }

        context.clearRect(0, 0, canvas.width, canvas.height);

        const gradient = context.createLinearGradient(0, 0, canvas.width, canvas.height);
        gradient.addColorStop(0, '#f0f9ff');
        gradient.addColorStop(1, '#e0f2fe');
        context.fillStyle = gradient;
        context.fillRect(0, 0, canvas.width, canvas.height);

        for (let i = 0; i < 12; i++) {
            context.strokeStyle = `rgba(30, 64, 175, ${Math.random() * 0.2 + 0.1})`;
            context.beginPath();
            context.moveTo(randomInt(0, canvas.width), randomInt(0, canvas.height));
            context.lineTo(randomInt(0, canvas.width), randomInt(0, canvas.height));
            context.stroke();
        }

        context.font = 'bold 30px Georgia, serif';
        context.fillStyle = '#0f172a';

        let x = 16;
        for (const char of text) {
            const angle = (Math.random() - 0.5) * 0.35;
            const y = randomInt(40, 55);
            context.save();
            context.translate(x, y);
            context.rotate(angle);
            context.fillText(char, 0, 0);
            context.restore();
            x += char === ' ' ? 10 : 18;
        }

        for (let i = 0; i < 80; i++) {
            context.fillStyle = `rgba(15, 23, 42, ${Math.random() * 0.25})`;
            context.fillRect(randomInt(0, canvas.width), randomInt(0, canvas.height), 1.5, 1.5);
        }
    }

    function generateCaptcha() {
        const challenge = buildChallenge();
        challengeSpan.textContent = 'Enter the result shown in the image.';
        drawCaptchaImage(challenge);
        answerInput.value = '';
        errorMessage.classList.add('hidden');
        attemptsMessage.classList.add('hidden');
    }

    function validateCaptcha() {
        const userAnswer = Number.parseInt(answerInput.value, 10);

        if (Number.isNaN(userAnswer) || userAnswer !== expectedAnswer) {
            incorrectAttempts += 1;
            errorMessage.classList.remove('hidden');

            if (incorrectAttempts >= maxIncorrectAttempts) {
                attemptsMessage.classList.remove('hidden');
            }

            return false;
        }

        incorrectAttempts = 0;
        errorMessage.classList.add('hidden');
        attemptsMessage.classList.add('hidden');
        return true;
    }

    function refreshCaptcha() {
        incorrectAttempts = 0;
        generateCaptcha();
    }

    refreshButton.addEventListener('click', refreshCaptcha);
    generateCaptcha();

    window.Captcha = {
        validateCaptcha,
        refreshCaptcha
    };
})();
