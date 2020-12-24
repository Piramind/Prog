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
