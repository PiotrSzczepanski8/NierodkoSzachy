object Form3: TForm3
  Left = 0
  Top = 0
  Caption = 'Nierodkoszachy'
  ClientHeight = 699
  ClientWidth = 858
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  TextHeight = 15
  object Label1: TLabel
    Left = 174
    Top = 24
    Width = 235
    Height = 33
    Caption = 'NierodkoSzachy'
    Font.Charset = EASTEUROPE_CHARSET
    Font.Color = clWindowText
    Font.Height = -23
    Font.Name = '@Dela Gothic One'
    Font.Style = []
    ParentFont = False
  end
  object Label2: TLabel
    Left = 632
    Top = 158
    Width = 174
    Height = 15
    Caption = 'Podaj czas trwania partii (w min):'
  end
  object StringGrid1: TStringGrid
    Left = 32
    Top = 80
    Width = 529
    Height = 529
    ColCount = 8
    DefaultRowHeight = 64
    FixedCols = 0
    RowCount = 8
    FixedRows = 0
    TabOrder = 0
  end
  object Button1: TButton
    Left = 32
    Top = 632
    Width = 97
    Height = 25
    Caption = 'Obr'#243#263' plansz'#281
    TabOrder = 1
  end
  object Button2: TButton
    Left = 144
    Top = 632
    Width = 97
    Height = 25
    Caption = 'Poddaj parti'#281
    TabOrder = 2
  end
  object Edit1: TEdit
    Left = 632
    Top = 187
    Width = 105
    Height = 23
    TabOrder = 3
    Text = '5'
  end
  object Button3: TButton
    Left = 632
    Top = 232
    Width = 75
    Height = 25
    Caption = 'Graj'
    TabOrder = 4
  end
end
