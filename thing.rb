puts "What's your name?"
name = gets.chomp
puts "How many times have you revolved around the sun #{name}?"
number = gets.to_i

if number >= 2
puts "Oh? You are #{number} years older than me!"
elsif number == 1 || number == 0
puts "huh, we are the same age, you and I."
else
puts "I'm not sure that's the answer i was looking for, think about your answer and try again later!"

end