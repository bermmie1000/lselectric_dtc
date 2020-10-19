const time = document.querySelector('.clock')

function getTime() {
    const date = new Date();
    const hour = date.getHours();
    const minute = date.getMinutes();
    const second = date.getSeconds();

    function getTwoDigit(number) {
        result = number < 10 ? `0${number}` : `${number}`;
        return result;
    }
    time.innerText = `${getTwoDigit(hour)}:${getTwoDigit(minute)}:${getTwoDigit(second)}`;
}




function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();