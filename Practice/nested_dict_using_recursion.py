def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


data = {
    "type": "video",
    "videoID": "vid001",
    "links": [
        {"type": "video", "videoID": "vid002", "links": []},
        {"type": "video",
         "videoID": "vid003",
         "links": [
             {"type": "video", "videoID": "vid004"},
             {"type": "video", "videoID": "vid005"},
         ]
         },
        {"type": "video", "videoID": "vid006"},
        {"type": "video",
         "videoID": "vid007",
         "links": [
             {"type": "video", "videoID": "vid008", "links": [
                 {"type": "video",
                  "videoID": "vid009",
                  "links": [{"type": "video", "videoID": "vid010"}]
                  }
             ]}
         ]},
    ]
}
output = []
for i in item_generator(data, "videoID"):
    ans = {"videoID": i}
    output.append(ans)

print(output)
