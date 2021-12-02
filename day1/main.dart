import 'dart:convert';
import 'dart:io';

main() {
  execute();
}

void execute() async {
  List<int> processed = [];
  int last = 0;

  int count = 0;

  final List<String> data = await new File("_data.txt")
      .openRead()
      .transform(utf8.decoder)
      .transform(new LineSplitter())
      .toList();

  data.forEach((e) {
    int _sum = 0;
    final _list = data.skip(count).take(3);
    _list.forEach((element) => _sum += int.parse(element));
    count++;

    if (_sum > last && last > 0) {
      processed.add(_sum);
    }
    last = _sum;

    print(_list);
    print(count);
  });

  // data.forEach((element) {
  //   final number = int.parse(element);
  // if (number > last && last > 0) {
  //   processed.add(number);
  // }
  // last = number;
  // });

  print(" ${processed.toString()} ${processed.length} ${data.length}");
}
