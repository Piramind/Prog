require 'date'


class PhoneBook
  attr_accessor :country, :birthday, :organization, :position

  def initialize(second_name, first_name, father_name, number, params={})
    @second_name = second_name
    @first_name = first_name
    @father_name = father_name
    @number = number
    self.set_country(params.fetch(:country, nil))
    self.set_birthday(params.fetch(:birthday, nil))
    self.set_organization(params.fetch(:organization, nil))
    self.set_position(params.fetch(:position, nil))

    is_valid = self.validate()

    if is_valid
      db = DBFetcher.new()
      db.сonnect()
    else
      raise Exception.new "Невалидные данные"
    end
  end

  def set_country(country_name)
    if Validator.new().validate_country(country_name)
      @country_name = country_name
    else
      puts 'Такой страны нет'
    end
  end

  def set_birthday(birthday)
    if Validator.new().validate_birthday(birthday)
      @birthday = birthday
    else
      puts 'Неверный формат даты рождения'
    end
  end

  def set_organization(organization)
    if Validator.new().validate_organization(organization)
      @organization = organization
    else
      puts 'Название организации не должно содержать цифр'
    end
  end

  def set_position(position)
    if Validator.new().validate_position(position)
      @position = position
    else
      puts 'Название должности не должно содержать цифр'
    end
  end

  def validate
    validator = Validator.new()
    verdicts = []
    verdicts.append(validator.validate_name(@second_name))
    verdicts.append(validator.validate_name(@first_name))
    verdicts.append(validator.validate_name(@father_name))
    verdicts.append(validator.validate_telephone(@number))
    verdicts.append(validator.validate_country(@country))
    verdicts.append(validator.validate_birthday(@birthday))
    verdicts.append(validator.validate_organization(@organization))
    verdicts.append(validator.validate_position(@position))

    return !(verdicts.include? false)
  end
end


class Validator
  def validate_name(name)
    return name.count("0-9") == 0
  end

  def validate_telephone(number)
    return number.count("a-zA-Z") == 0
  end

  def validate_birthday(birthday)
    """ birthday date like 04-04-2001 """
    if(birthday.nil?) return true

    begin
       Date.parse(birthday)
       return true
    rescue ArgumentError
       return false
    end
  end

  def validate_country(country_name)
    return country_name.nil? || Countries.include?(country_name)
  end

  def validate_organization(organization_name)
    return organization_name.nil? || organization_name.count("0-9") == 0
  end

  def validate_position(position_name)
    return position_name.nil? || position_name.count("0-9") == 0
  end
end


class Countries
  COUNTRIES = ['Russia', 'China', 'India', 'USA', 'Japan', 'German', 'Poland', 'Italy', 'Poland', 'Czech']

  def include?(country_name)
    return self.COUNTRIES.include? country_name
  end
end


class DBFetcher
  def сonnect()
    return 'Успешное подключение к базе'
  end

  def fetch(sql_imitation)
    return true
  end
end


class DBHandle
  def convert(array)
    return array.join(';')
  end
end
