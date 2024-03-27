import json

# 颜色规约映射
color_mapping = {
    "Black": ["Black", "Midnight", "Graphite", "Jet Black", "Matte Black", "BlackSlate", "Black Titanium"],
    "White": ["White", "Starlight", "WhiteSilver", "White Titanium"],
    "Gold": ["Gold"],
    "Silver": ["Silver"],
    "Pink": ["Pink", "Rose Gold"],
    "Gray": ["Gray", "Space Gray", "Natural Titanium"],
    "Blue": ["Blue", "Sierra Blue", "Pacific Blue", "Blue Titanium"],
    "Red": ["Red"],
    "Green": ["Green", "Alpine Green"],
    "Yellow": ["Yellow"],
    "Purple": ["Purple", "Deep Purple"],
    "Orange": ["Coral"]
}

# 读取 JSON 文件
with open("iphone.json", "r") as file:
    data = json.load(file)

# 构建 Model 到 Color 的映射
model_to_color = {}
for generation in data:
    for model in generation["Models"]:
        for m in model["Model"]:
            for color, mapped_colors in color_mapping.items():
                if any(mapped_color.lower() in model["Color"].lower() for mapped_color in mapped_colors):
                    model_to_color[m] = color

# 输出 Model 到 Color 的映射到文件
with open("model_to_color.json", "w") as outfile:
    json.dump(model_to_color, outfile, indent=4)

print("Model 到 Color 的映射已写入到 model_to_color.json 文件中")