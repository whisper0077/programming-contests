t=gets.to_i
t.times do |i|
  n=gets.to_i
  selled=[0]*n
  favors=[0]*n
  n.times do |ni|
    input = gets.chomp.split(" ").map(&:to_i)
    fs = input[1..-1].select{|f| selled[f]==0}
    
    if fs.size>0
      s = fs.select{|f| favors[f]==0}.sort{|f| favors[f]}.first
      s = fs.sort{|f| favors[f]}.first if s==nil
      puts s
      selled[s]=1
    else
      puts -1
    end

    fs.each do |f|
      favors[f]+=1
    end

    $stdout.flush
  end
end