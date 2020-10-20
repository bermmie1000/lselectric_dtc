

function input() {
    const name = document.querySelector('.name').value;
    name = addEventListener(name);

    return name;
}




function init() {
    input();
}

init();

/* 변경된 부분 표시 */