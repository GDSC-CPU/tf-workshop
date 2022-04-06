# <logos-tensorflow /> Lite <twemoji-red-heart /><twemoji-blue-heart /><twemoji-green-heart /><twemoji-yellow-heart /> <logos-flutter /> (<logos-dart /><logos-flutter /> Flutter side)

- follow OS-specific instructions at:
  https://pub.dev/packages/tflite_flutter
- create an `assets/` directory on your Flutter app, if it doesn't exist
- put the `min-max.json` and `model.tflite` files there
- _"declare"_ those files in `pubspec.yaml`
  ```yaml
  flutter:
    # The following line ensures that the Material Icons font is
    # included with your application, so that you can use the icons in
    # the material Icons class.
    uses-material-design: true

    # To add assets to your application, add an assets section, like this:
    assets:
      - assets/foo.tflite
      - assets/min-max.json
    ```
- Install `tflite_flutter`:
  ```yaml
  cupertino_icons: ^1.0.2
  tflite_flutter: ^0.9.0
  ```