' FormatReport.bas - import in Word: Alt+F11 > File > Import File
' Applies a consistent look to the active document.
Sub FormatReport()
    Dim doc As Document
    Set doc = ActiveDocument

    With doc.Styles(wdStyleNormal).Font
        .Name = "Calibri"
        .Size = 11
    End With
    With doc.Styles(wdStyleHeading1).Font
        .Name = "Calibri Light"
        .Size = 18
        .Color = RGB(31, 78, 121)
    End With

    ' Page numbers in the footer of every section
    Dim s As Section
    For Each s In doc.Sections
        s.Footers(wdHeaderFooterPrimary).PageNumbers.Add _
            PageNumberAlignment:=wdAlignPageNumberCenter
    Next s

    MsgBox "Report formatted: " & doc.Paragraphs.Count & " paragraphs.", vbInformation
End Sub
