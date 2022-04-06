# <logos-tensorflow /> Lite <twemoji-red-heart /><twemoji-blue-heart /><twemoji-green-heart /><twemoji-yellow-heart /> <logos-flutter /> (<logos-dart /><logos-flutter /> Flutter side)

- Write your own scaling code:
  ```dart
  List scale(List<List<double>> input, mins, maxes) { /* ... */ }
  ```
- Predict away!
  ```dart
  final interpreter = await tfl.Interpreter.fromAsset('foo.tflite');
  final json = await rootBundle.loadString('assets/min-max.json');
  var minMax = jsonDecode(json);
  var input = [
    [65.0, 55.0]
  ];
  var scaledInput = scale(input, minMax['x_min'], minMax['x_max']);
  print('scaled: ${scaledInput}');

  var output = List.filled(1, 0).reshape([1, 1]);
  interpreter.run(scaledInput, output);

  if (output[0][0] >= 0.5) {
    print('admitted! ${output[0][0] * 100}%');
  } else {
    print('not admitted! ${output[0][0] * 100}%');
  }
  ```