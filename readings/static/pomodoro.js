const timer = {
  pomodoro: 25,
  break: 5,
};

let interval;

const mainButton = document.getElementById('js-start-btn');
    mainButton.addEventListener('click', () => {
        const { action } = mainButton.dataset;
        if (action === 'start') {
            startTimer();
        }
        else {
            stopTimer();
        }
});

const modeButtons = document.querySelector('#js-mode-buttons');
modeButtons.addEventListener('click', handleMode);

function handleMode(event) {
    const { mode } = event.target.dataset;

    if (!mode) {
        return;
    } else {
        switchMode(mode);
        stopTimer();
    }
}

function switchMode(mode) {
    timer.mode = mode;
    timer.remainingTime = {
        total: timer[mode] * 60,
        minutes: timer[mode],
        seconds: 0,
    };

    document.querySelectorAll('button[data-mode]')
    document.querySelector(`[data-mode="${mode}"]`)

    updateClock();
}

function updateClock() {
    const { remainingTime } = timer;

    // Always making sure that there are two digits for time
    // 5 seconds will be 05
    const minutes = `${remainingTime.minutes}`.padStart(2, '0');
    const seconds = `${remainingTime.seconds}`.padStart(2, '0');

    // Assigning the contents of the elements displayed on the webpage and changing them
    const min = document.getElementById('js-minutes');
    const sec = document.getElementById('js-seconds');
    min.textContent = minutes;
    sec.textContent = seconds;
}

function getRemainingTime(endTime) {
    const currentTime = Date.parse(new Date());
    const difference = endTime - currentTime;

    const total = Number.parseInt(difference / 1000, 10);

    // Changing time to 60 second/minute format
    const minutes = Number.parseInt((total / 60) % 60, 10);
    const seconds = Number.parseInt(total % 60, 10);

    return {
        total,
        minutes,
        seconds,
    };
}

function stopTimer() {
    clearInterval(interval);

    mainButton.dataset.action = 'start';
    mainButton.textContent = 'Start';
}

function startTimer() {
    let { total } = timer.remainingTime;
    const endTime = Date.parse(new Date()) + total * 1000;

    // Changing the main button to a stop button that can pause the timer
    mainButton.dataset.action = 'stop';
    mainButton.textContent = 'Stop';

    // Starting the countdown and updating it every 1000 milliseconds
    interval = setInterval(function() {
        timer.remainingTime = getRemainingTime(endTime);
        updateClock();

        total = timer.remainingTime.total;
        if (total <= 0) {
            clearInterval(interval);
        }

        // Alerting the user to take a break once 25 minutes have passed and automatically switches to the break mode
        if (total === 0) {
            switchMode('break');
            stopTimer()
            alert('Time for a 5 minute break!');
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', () => {
    switchMode('pomodoro');
});