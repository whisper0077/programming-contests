t=gets.to_i 
t.times do |i|
  a = gets.to_i
  rect = a==20 ? [3,7] : [3,67]
  ocd = [0]*(rect[0]*rect[1])
  puts "10 10"
  $stdout.flush
  sx,sy = gets.split(" ").map(&:to_i)
  loop do
    f = [0,[0,0]]
    1.upto(rect[0]-2) do |y|
      1.upto(rect[1]-2) do |x|
        n = 0
        (y-1).upto(y+1) do |yy|
          (x-1).upto(x+1) do |xx|
            n += 1 if ocd[yy*rect[1]+xx]==0
          end
        end
        if n>f[0]
          f = [n, [sx+x,sy+y]]
        end
      end
    end
    puts f[1].join(" ")
    $stdout.flush
    tx, ty = gets.split(" ").map(&:to_i)
    break if tx==0&&ty==0
    
    ocd[(ty-sy)*rect[1]+tx-sx] = 1
  end
end