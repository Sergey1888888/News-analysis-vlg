#encoding "utf-8"

S -> Word<kwtype="фио"> interp (Person.FIO::not_norm);
Text -> AnyWord* S AnyWord*;
Text2 -> Text interp (Person.Text::not_norm);
