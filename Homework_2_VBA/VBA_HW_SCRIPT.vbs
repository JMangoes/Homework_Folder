Sub Stockmarket()
    For Each ws In Worksheets
        Dim WorksheetName As String
        WorksheetName = ws.Name
    
    
        ws.Range("J1").Value = "Ticker"
        ws.Range("K1").Value = "Yearly Change"
        ws.Range("L1").Value = "Percent Change"
        ws.Range("M1").Value = "Total Stock Volume"
        
        Dim ticker_name As String
        Dim summary As Integer
        summary = 2
        Dim year_change As Double
        Dim year_total As Double
        year_total = 0
        Dim percentchange As Double
        Dim volume As Double
        volume = 0
        
        year_change = ws.Cells(summary, 3).Value
        
        
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    
        For i = 2 To LastRow
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
                ticker_name = ws.Cells(i, 1).Value
                ws.Range("J" & summary).Value = ticker_name
                
                year_total = year_total + (ws.Cells(i, 6).Value - year_change)
                ws.Range("K" & summary).Value = year_total
                
                percentchange = (year_total / year_change)
                ws.Range("L" & summary).Value = percentchange
                ws.Range("L" & summary).Style = "Percent"
                
                volume = volume + ws.Cells(i, 7).Value
                ws.Range("M" & summary).Value = volume
                
                summary = summary + 1
                year_total = 0
                year_change = ws.Cells(summary, 3).Value
            End If
            
              If ws.Cells(i, 11).Value >= 0 Then
                    ws.Cells(i, 11).Interior.ColorIndex = 4
                    
              Else
                    ws.Cells(i, 11).Interior.ColorIndex = 3
                    
              End If
            
        
        Next i
        
    Next ws
    
    
    
    
End Sub

