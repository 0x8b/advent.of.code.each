require 'set'

all_allergens = Set[]
all_ingredients = Set[]

occurrence_counter = Hash.new { |hash, key| hash[key] = 0 }

foods = File.open("../../data/2020/21.txt").each_line.map do |line|
  food = line.scan /\w+/
  ci = food.index "contains"

  allergens = food[ci..][1..]
  ingredients = food[...ci]

  all_allergens.merge allergens
  all_ingredients.merge ingredients

  for ingredient in ingredients
    occurrence_counter[ingredient] += 1
  end

  [ingredients, allergens]
end

ingredient_could_be = Hash.new { |hash, key| hash[key] = Set[] }

for ingredient in all_ingredients
  ingredient_could_be[ingredient].merge all_allergens
end

for ingredients, allergens in foods
  for allergen in allergens
    for ingredient in all_ingredients
      if ingredients.none? ingredient
        ingredient_could_be[ingredient].delete allergen
      end
    end
  end
end

part_1 = ingredient_could_be.sum { |ingredient, allergens| allergens.empty? ? occurrence_counter[ingredient] : 0 }

puts part_1


variants = ingredient_could_be.to_a.reject { |_, allergens| allergens.empty? }

matches = []

while (ingredient, allergens = variants.find { |ingredient, allergens| allergens.size == 1 })
  allergen = allergens.first

  matches << [ingredient, allergen]

  variants.map! { |ingredient, allergens| [ingredient, allergens.delete(allergen)] }
end


part_2 = matches.sort_by(&:last).map(&:first).join(?,)

puts part_2
