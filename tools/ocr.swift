import Foundation
import Vision
import AppKit

let url = URL(fileURLWithPath: CommandLine.arguments[1])
let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.usesLanguageCorrection = false
let handler = VNImageRequestHandler(url: url, options: [:])
try handler.perform([request])
let image = NSImage(contentsOf: url)!
let rep = NSBitmapImageRep(data: try Data(contentsOf: url))!
let width = Double(rep.pixelsWide)
let height = Double(rep.pixelsHigh)
let rows: [[String: Any]] = (request.results ?? []).compactMap { result in
    guard let candidate = result.topCandidates(1).first else { return nil }
    let box = result.boundingBox
    return ["text": candidate.string,
            "x": box.minX * width, "y": (1 - box.maxY) * height,
            "w": box.width * width, "h": box.height * height]
}
let data = try JSONSerialization.data(withJSONObject: rows, options: [.sortedKeys])
print(String(data: data, encoding: .utf8)!)
