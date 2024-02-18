def main():
    file = input("File name: ").strip().lower()
    parts = file.split(".")
    if len(parts) > 1:
        ending = parts[-1]
        match ending:
            case "pdf" | "zip":
                print("application/" + ending)
            case "png" | "gif" :
                print("image/" + ending)
            case "jpg" | "jpeg":
                print("image/jpeg")
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")


main()