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
