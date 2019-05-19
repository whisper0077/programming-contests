# small のみ
t=gets.to_i
sqrt2 = Math.sqrt(2)
t.times do |i|
  a = gets.to_f
  rad = Math.acos(a/sqrt2) - 45.0*Math::PI/180.0
  x = [0.5*Math.cos(rad), 0.5*Math.sin(rad), 0].map{|v| v.round(10)}
  y = [0.5*Math.cos(rad+Math::PI/2.0), 0.5*Math.sin(rad+Math::PI/2.0), 0].map{|v| v.round(10)}
  puts "Case ##{i+1}:"
  puts x.join(" ")
  puts y.join(" ")
  puts "0 0 0.5"
end