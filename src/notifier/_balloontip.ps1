# 准备接受的外部参数，必须放在函数前面
param($Text, $Title = 'Information', $Icon = 'Info', $ExpirationMinutes = 0)
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

function ShowBalloonTipInfo
{
    [CmdletBinding()]
    param
    (
    # Mandatory=$true 参数表示必选参数
        [Parameter(Mandatory, Position = 0)] [string] $Text,
        [Parameter(Position = 1)] [string] $Title = 'title',
    # It must be 'None','Info','Warning','Error'
        [Parameter(Position = 2)] [string] $Icon = 'Info',
    # 这个参数没有使用
        [Parameter(Position = 3)] [int] $ExpirationMinutes = 0
    )
    Add-Type -AssemblyName System.Windows.Forms
    $balloonToolTip = New-Object System.Windows.Forms.NotifyIcon
    $balloonToolTip.Icon = [System.Drawing.SystemIcons]::Information
    $balloonToolTip.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::$Icon
    $balloonToolTip.BalloonTipText = $Text
    $balloonToolTip.BalloonTipTitle = $Title
    $balloonToolTip.Visible = $true
    $balloonToolTip.ShowBalloonTip(1000*20)  # 默认单位是毫秒
    #    Start-Sleep -Seconds 1
    #    $balloonToolTip.Dispose()
}
# 调用函数，接收传递进来的参数
ShowBalloonTipInfo $Text $Title  $Icon $ExpirationMinutes
