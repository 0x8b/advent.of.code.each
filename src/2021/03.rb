report = ARGF.read.lines.map { _1.chomp.chars }

W = report.first.size

gamma = report.transpose.map { 2 * _1.count(?1) > report.size ? ?1 : ?0 }.join

epsilon = gamma.tr "01", "10"

part_1 = gamma.to_i(2) * epsilon.to_i(2)

puts part_1

ogr = (0...W).inject(report) { |r, i|
  break r if r.size == 1

  r.select {
    _1[i] == (2 * r.count { |rr| rr[i] == ?1 } >= r.size ? ?1 : ?0)
  }
}.first.join.to_i 2

csr = (0...W).inject(report) { |r, i|
  break r if r.size == 1

  r.select {
    _1[i] == (2 * r.count { |rr| rr[i] == ?0 } <= r.size ? ?0 : ?1)
  }
}.first.join.to_i 2

part_2 = ogr * csr

puts part_2
