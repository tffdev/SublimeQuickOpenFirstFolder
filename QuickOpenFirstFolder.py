import os
import sublime
import sublime_plugin

items = []

class PopupFirstFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		items.clear()
		folders = self.window.folders()
		if len(folders) > 0:
			for root, subdirs, files in os.walk(folders[0]):
				for file in files:
					items.append([file, root + "/" + file])
		self.window.show_quick_panel(items, on_select=self.done)
		
	def done(self, result):
		if result >= 0:
			self.window.open_file(items[result][1])
