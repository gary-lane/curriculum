class CountingMachine:
  def __init__(self) -> None:
    self.count = 0

  def inc(self) -> None:
    self.count += 1

  def dec(self) -> None:
    self.count -= 1