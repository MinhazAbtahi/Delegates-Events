import wmi

window_manager = wmi.WMI ()

# prints os info 
for os in window_manager.Win32_OperatingSystem():
	print ("OS: " + os.Caption + '\n')
	
# prints newly created processes
active_process_watcher = window_manager.Win32_Process.watch_for("operation")
stopped_process_watcher = window_manager.Win32_Process.watch_for("deletion")
new_process_watcher = window_manager.Win32_Process.watch_for("creation")

while True:
	# new processes
	new_process = new_process_watcher()
	print "New Process: " + new_process.Caption
	
	# stopped processes
	stopped_process = stopped_process_watcher()
	print 'Stopped Process: ' + stopped_process.Caption
	