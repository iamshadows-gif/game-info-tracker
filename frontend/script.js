fetch("http://127.0.0.1:8000/games")
    .then(response => response.json())
    .then(data => {

        const gamesContainer = document.getElementById("games");

        data.forEach(game => {
            const gameElement = document.createElement("p");

            gameElement.textContent = game.name;

            gamesContainer.appendChild(gameElement);
        });

    });