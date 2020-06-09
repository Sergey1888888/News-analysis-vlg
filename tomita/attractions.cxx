#encoding "utf-8"

S -> Word<kwtype="дост_названия"> interp (Attractions.Name::not_norm);
Text -> AnyWord* S AnyWord*;
Text2 -> Text interp (Attractions.Text::not_norm);
