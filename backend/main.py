from database.game_functions import (
    add_game,
    add_platform,
    add_game_platform,
    get_games,
    get_game,
    update_game,
    delete_game,
    get_platforms,
    get_platform,
    del_platform,   
    get_game_with_platform
)

while True:

    print("\n===== GAME INFO TRACKER =====")
    print("1. Add game")
    print("2. View all games")
    print("3. View one game")
    print("4. Update game rating")
    print("5. Delete game")
    print("6. View game along with platform")
    print("7. Add platform to game")
    print("8. View all platforms")
    print("9. View one platform")
    print("10.Delete platform")
    print("11.Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Game name: ")
        release_date = input("Release date: ")
        developer = input("Developer: ")
        publisher = input("Publisher: ")
        rating = float(input("Rating: "))

        add_game(name, release_date, developer, publisher, rating)

    elif choice == "2":
        games = get_games()

        if not games:
            print("No games found")
        else:
            for game in games:
                id, name, release_date, developer, publisher, rating = game
                print(f"ID: {id}")
                print(f"Name: {name}")
                print(f"Release Date: {release_date}")
                print(f"Developer: {developer}")
                print(f"Publisher: {publisher}")
                print(f"Rating: {rating}")
                print("--------------------")

    elif choice == "3":
        game_id = int(input("Enter the game ID to view: "))
        game = get_game(game_id)

        if not game:
            print("Game not found!")

        else:
            id, name, release_date, developer, publisher, rating = game
            print(f"ID: {id}")
            print(f"Name: {name}")
            print(f"Release Date: {release_date}")
            print(f"Developer: {developer}")
            print(f"Publisher: {publisher}")
            print(f"Rating: {rating}")
            print("--------------------")

    elif choice == "4":
        rating = float(input("Enter the rating of the game: "))
        game_id = int(input("Enter the id of the game to be updated: "))
        game = get_game(game_id)

        if not game:
            print("Enter valid id")

        else:
            update_game(game_id, rating)
            print("Info Updated")

    elif choice == "5":
        game_id = int(input("Enter the game ID to delete: "))
        game = get_game(game_id)

        if not game:
            print("No record of the game was found!")

        else:
            delete_game(game_id)
            print("Info deleted successfully!")


    elif choice == "6":
        game_id = int(input("Enter the game id to be searched with platform: "))
        games = get_game_with_platform(game_id)

        if not games:
            print("No platform found for this game")

        else:
            for game in games:
                name, platform = game
                print(f"Game: {name}")
                print(f"Platform: {platform}")
                print("--------------------")

    elif choice == "7":
        game_id = int(input("Enter game ID: "))
        platform_id = int(input("Enter platform ID: "))
        games = get_game(game_id)

        if not games:
            print("No game found for the record to be added")

        else:
            add_game_platform(game_id,platform_id)


    elif choice == "8":
        platforms = get_platforms()

        if not platforms:
            print("No platforms found")

        else:
            for platform in platforms:
                id, name = platform
                print(f"ID: {id}")
                print(f"Name: {name}")
                print("--------------------")


    elif choice == "9":
        platform_id = int(input("Enter platform ID: "))
        platform = get_platform(platform_id)

        if not platform:
            print("Platform not found")

        else:
            id, name = platform
            print(f"ID: {id}")
            print(f"Name: {name}")
            print("--------------------")


    elif choice == "10":
        platform_id = int(input("Enter platform ID to delete: "))
        platform = get_platform(platform_id)

        if not platform:
            print("Platform not found")

        else:
            delete_platform(platform_id)
            print("Platform deleted successfully!")


    elif choice == "11":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")


