import wx

# Track progress in an iterable with a progress box
def progress_box(function, iterable, window_title):
    app = wx.PySimpleApp()
    dialog = wx.ProgressDialog(
        window_title, "Time remaining", len(iterable),
        style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME
    )
    for index, item in enumerate(iterable):
        dialog.Update(index)
        function(item)
    dialog.Update(index)
    # ! REMOVE wx.Sleep(1)
    dialog.Destroy()
