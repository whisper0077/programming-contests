t=gets.to_i

def calc(s)
  r=0
  a=1
  s.length.times do |i|
    r+=a if s[i]=="S"
    a*=2 if s[i]=="C"
  end
  r
end 

t.times do |ti|
  d, s = gets.chomp.split(" ")
  d = d.to_i 
  found = false
  ans = 0
  swap = true
  loop do
    b = calc(s)
    if b<=d
      found = true
      break
    end
    break unless swap

    swap = false
    (s.length-1).downto(1) do |i|
      if s[i]=="S" && s[i-1]=="C"
        ans += 1
        s[i],s[i-1] = s[i-1],s[i]
        swap = true
        break 
      end
    end
  end

  ans = "IMPOSSIBLE" unless found
  puts "Case ##{ti+1}: #{ans}"
end