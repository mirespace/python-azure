# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

POWERSHELL_INVALID_OPERATION_EXCEPTION = """#< CLIXML
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><Obj S="progress" RefId="0"><TN RefId="0"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N="SourceId">1</I64><PR N="Record"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><Obj S="progress" RefId="1"><TNRef RefId="0" /><MS><I64 N="SourceId">2</I64><PR N="Record"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><S S="Error">Get-AzAccessToken : Run Connect-AzAccount to login._x000D__x000A_</S><S S="Error">At line:11 char:10_x000D__x000A_</S><S S="Error">+ $token = Get-AzAccessToken -ResourceUrl 'scope'_x000D__x000A_</S><S S="Error">+          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_x000D__x000A_</S><S S="Error">    + CategoryInfo          : CloseError: (:) [Get-AzAccessToken], PSInvalidOperationException_x000D__x000A_</S><S S="Error">    + FullyQualifiedErrorId : Microsoft.Azure.Commands.Profile.GetAzureRmAccessTokenCommand_x000D__x000A_</S><S S="Error"> _x000D__x000A_</S></Objs>"""
POWERSHELL_NOT_LOGGED_IN_ERROR = """#< CLIXML
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">_x001B_[91mGet-AzAccessToken: _x000D__x000A_</S><S S="Error">_x001B_[96mLine |_x000D__x000A_</S><S S="Error">_x001B_[96m  11 | _x001B_[0m $token = _x001B_[96mGet-AzAccessToken -ResourceUrl 'scope'_x001B_[0m_x000D__x000A_</S><S S="Error">_x001B_[96m     | _x001B_[91m          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_x000D__x000A_</S><S S="Error">_x001B_[91m_x001B_[96m     | _x001B_[91mRun Connect-AzAccount to login._x001B_[0m_x000D__x000A_</S></Objs>"""
