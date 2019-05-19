t=gets.to_i
t.times do |ti|
  ans = "OK"
  n = gets.to_i 
  vi = gets.split(" ").map(&:to_i)
  vic = {}
  vi.each_with_index do |v,i|
    vic[v]||=[0,0]
    vic[v][i%2]+=1   
  end
  vsi = vi.sort

  vsi.each_with_index do |v,i|
    if vic[v][i%2] > 0
      vic[v][i%2]-=1
    else
      ans = i
      break
    end
  end
  puts "Case ##{ti+1}: #{ans}"
end