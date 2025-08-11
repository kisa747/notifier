#param($Message, $Title = 'Information', $Icon = 'Info')

$PSDefaultParameterValues['*:Encoding'] = 'utf8'
Function New-DotNetToast
{
    [cmdletBinding()]
    Param(
        [Parameter(Mandatory, Position = 0)]
        [String] $Message,
        [Parameter(Position = 1)]
        [String] $Title = 'Information',
        [Parameter(Position = 2)]
        [String] $Icon = 'Info',  # 可选参数：Info,Warning,Error
        [Parameter(Position = 3)]
        [Int] $ExpirationMinutes = 0
    )

    $IconPath = "$PSScriptRoot\images\$Icon.ico"
    $XmlString = @"
  <toast>
    <visual>
      <binding template="ToastGeneric">
        <text>$Title</text>
        <text>$Message</text>
        <image src="$IconPath" placement="appLogoOverride" hint-crop="circle" />
      </binding>
    </visual>
    <audio src="ms-winsoundevent:Notification.Default" />
  </toast>
"@
    #    $AppId = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
    $AppId = (Get-StartApps | Where-Object Name -eq "Windows PowerShell").AppID
    $null = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
    $null = [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]

    $ToastXml = [Windows.Data.Xml.Dom.XmlDocument]::new()
    $ToastXml.LoadXml($XmlString)

    $Toast = [Windows.UI.Notifications.ToastNotification]::new($ToastXml)

    # 默认通知在通知中心保留3天
    Write-Debug "ExpirationMinutes --> $ExpirationMinutes"
    if ($ExpirationMinutes -gt 0)
    {
        $ExpirationTime = [System.DateTime]::Now.AddMinutes($ExpirationMinutes)
        Write-Debug "ExpirationTime --> $ExpirationTime"
        $Toast.ExpirationTime = $ExpirationTime
    }
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($AppId).Show($Toast)
}

#New-DotNetToast $Message $Title $Icon
