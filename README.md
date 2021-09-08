# Webcam Photo Sharer

An app that starts the computer webcam, lets the user capture a photo,
upload the photo to the web (on FileStack) and creates a sharable link.

This app requires an API key for [FileStack](https://filestack.com).
You can sign up for free and access your API key at the [dev portal](https://dev.filestack.com).

This app uses [kivy](https://kivy.org) for its user interface, allowing you to capture webcam
screenshots and generate shareable links using simple graphical controls.

```shell
$ export FILESTACK_API_KEY=<API KEY>
$ python3 main.py
```
