const clockContainer = document.querySelector(".js-clock");
const clockTitle = clockContainer.querySelector('h1');

function getTime() {
    const date = new Date();
    const hour = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();

    function getTwoDigit(time) {
        result = time < 10 ? `0${time}` : `${time}`;
        return result;
    }
    clockTitle.innerText = `${getTwoDigit(hour)}:${getTwoDigit(minutes)}:${getTwoDigit(seconds)}`;
}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();