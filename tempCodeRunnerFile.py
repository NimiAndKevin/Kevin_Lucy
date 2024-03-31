speak_properly(f"I can see a {class_list[int(clsID)]}")
        detected_objects_count += 1
        speak_properly(f"I have seen {detected_objects_count} things")
        subprocess.run(['python', "C:\\Users\\surface\\Desktop\\gui.py"])
        break