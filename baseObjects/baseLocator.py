from __future__ import annotations

class Locator:

	def __init__(self, l_type, selector):
		self.l_type = l_type
		self.selector = selector
		self._original_selector = selector

	def parameterize(self, *args) -> Locator:
		return Locator(self.l_type, self.selector.format(*args))
