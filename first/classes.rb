class CustomFile < File
  def absolute_path(path)
    return super.absolute_path(path)
  end

  def is_catalog?(path)
    return super.directory?(path)
  end

  def exist?(path)
    return super.exist?(path)
  end

  def modified_time(path)
    return super.atime(path)
  end
end


class CustomHash < Hash
  def delete_by()
    self.keys.each{|key|
      if yield(key, self[key])
        self.delete(key)
      end
    }
    return self
  end

  def is_empty?()
    return self.empty?()
  end
end


class CustomSymbol < Symbol
  def all_symbols
    return super.all_symbols
  end

  def between(a, b, c)
    return b <= a and a <= c
  end
end


class CustomTime < Time
  def now()
    return super.now()
  end

  def is_friday?()
    return Time.now().wday == 5
  end

  def utc_name()
    return Time.now().zone
  end
end
