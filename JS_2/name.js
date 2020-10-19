

function input() {
    const name = document.querySelector('.name').value;
    name = addEventListener(name);

    return name;
}




function init() {
    input();
}

init();