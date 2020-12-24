class CustomSymbol < Symbol
  def all_symbols
    return super.all_symbols
  end

  def between(a, b, c)
    return b <= a and a <= b
  end
end
