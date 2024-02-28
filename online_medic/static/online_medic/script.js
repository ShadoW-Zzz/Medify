document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.add-button').onclick = () => {
        let individual = document.querySelector('.individual').cloneNode(true);
        console.log("button clicked");
        document.querySelector('.all').appendChild(individual);
    };
});

