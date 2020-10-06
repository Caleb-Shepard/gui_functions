import wx

# This is a side effecting line that wx requires
wx.PySimpleApp()
# wx.App()

# Track progress in an iterable with a progress box
def progress_box(function, iterable, window_title):
    results = []
    dialog = wx.ProgressDialog(
        window_title, "Time remaining", len(iterable),
        style=wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME
    )
    # set index = 0 so no crash if enum is None
    index = 0
    if iterable is None:
        return results
    if len(iterable) == 0:
        return results
    for index, item in enumerate(iterable):
        dialog.Update(index)
        result = function(item)
        if type(result) is list:
            results.extend(result)
        else:
            results.append(result)
    dialog.Update(index)
    dialog.Destroy()
    return results

    
def error_dialog(message, title='error'):
    try:
        dlg = wx.MessageDialog(None,
            message=message,
            caption=title,
            style=wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()
    except wx._core.PyNoAppError:
        #don't want to build an app unless its necessary
        error_dialog(message, title)

        
# Create a "wxpython" file dialog to pick a file
def wx_pick_file(filetype_wildcard):
    try:
        dlg = wx.FileDialog(
            parent=None,
            message='Open File',
            wildcard=filetype_wildcard,
            defaultDir='%Documents%',
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_CANCEL:
            return None
        return dlg.GetPath()
    except wx._core.PyNoAppError:
        #don't want to build an app unless its necessary
        app = wx.App()
        wx_pick_file(filetype_wildcard)

        
# Create a "wxpython" file dialog to pick a file
def wx_pick_directory():
    try:
        dlg = wx.DirDialog(
            parent=None,
            message='Open Folder',
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_CANCEL:
            return None
        return dlg.GetPath()
    except wx._core.PyNoAppError:
        #don't want to build an app unless its necessary
        app = wx.App()
        wx_pick_directory()
