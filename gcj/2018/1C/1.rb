t=gets.to_i

def solve(lw,ns,ne,words,a)
  if ns==ne
    if words.include?(a)
      return nil
    else
      return a
    end
  end
  lw[ns].each do |w|
    r = solve(lw,ns+1,ne,words,a+w)
    return r if r
  end
  return nil
end 

t.times do |i|
  n,l = gets.chomp.split(" ").map(&:to_i)
  ans = "-"
  lw = Array.new(l)
  l.times{|li| lw[li]=[]}
  words = []
  n.times do |ni|
    w = gets.chomp.split("")
    words << w.join
    l.times do |li|
      lw[li] << w[li]
    end
  end

  l.times{|li| lw[li].uniq!}

  ans = solve(lw,0,l,words,"")
  ans||="-"
  puts "Case ##{i+1}: #{ans}"
end