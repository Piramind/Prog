puts "INREGER"
n = 8
r = -3
puts "модуль числа #{n} = #{n.abs}"
puts "модуль числа #{r} = #{r.abs}"


t = 0
y = 1
puts "проверка числа #{t} на  - #{t.zero?}" 
puts "проверка числа #{y} на  - #{y.zero?}" 


puts "Увеличить число #{y} на 1  - #{y>>-1}" 
puts "Увеличить число #{n} на 1  - #{n.next}"
print "\n"



puts "FLOAT"
w = 1.81111
y = 3
puts "Округление числа #{w} вниз #{w.floor}"
print "#{n} делить #{y} - #{n.digits(y)}"
print "\n"


 
puts "STRING"
string = "HELLO WORLD"
puts "Приведение к нижнему регистру - #{string.capitalize}"
puts "замена последнего элемента последующим символом - #{string.next}"
puts "Удаление предшествуюших или завершающих символов - #{string.chomp("lo world")}"
puts "Удаление предшествуюших или завершающих символов - #{"hello world\n".chomp}"
print "\n"

 
puts "ARRAY"
arr1 = ["asd", "gh","gh", "tf", "yt", "fgh"]
arr1.delete("gh")
print "Удаление всех символов 'gh' в массиве arr1-  #{arr1}"
print "\n"
print "в ранодмном порядке массива arr1 #{arr1.sample(arr1.length)}"
print "\n"
print "Массив arr1 в строку с соединяющим эементом-пробелом #{arr1.join(" ")}"
print "\n"
print "\n"




puts "HASH"
hash1 = { 1 => "Имя", 2=> "Фамилия" }
hash2 = { 3 => "Отчество", 4 => "Возраст" }

begin
	print hash1.fetch(1)
	print "\n"
rescue
	print hash1.fetch(3)
ensure
	print "Key '1' not found"
end
print "\n"
print hash1.include?(1)

print "\n"
print(hash1.merge!(hash2))
print "\n"
print "\n"


print "КОД"
range = (0..100)
print "\n"
print range.last
print "\n"

results = [10, 2, 5, 12, 11, 11, 4]
num = 1
for i in results
  puts "Value #{num}: Value #{i}"
  num += 1
end

puts(8.1111.truncate)