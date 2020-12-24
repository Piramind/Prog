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
