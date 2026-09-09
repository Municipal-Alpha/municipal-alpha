import Foundation
import Vision
import AppKit

let path = CommandLine.arguments[1]
guard let img = NSImage(contentsOfFile: path),
      let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    FileHandle.standardError.write("cannot load \(path)\n".data(using: .utf8)!)
    exit(1)
}
let W = CGFloat(cg.width), H = CGFloat(cg.height)
let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.usesLanguageCorrection = false
let handler = VNImageRequestHandler(cgImage: cg, options: [:])
do { try handler.perform([req]) } catch { exit(2) }

for case let obs as VNRecognizedTextObservation in (req.results ?? []) {
    guard let cand = obs.topCandidates(1).first else { continue }
    let s = cand.string
    var idx = s.startIndex
    while idx < s.endIndex {
        while idx < s.endIndex, s[idx] == " " { idx = s.index(after: idx) }
        if idx >= s.endIndex { break }
        var end = idx
        while end < s.endIndex, s[end] != " " { end = s.index(after: end) }
        let r = idx..<end
        if let box = try? cand.boundingBox(for: r) {
            let bb = box.boundingBox
            let x = bb.minX * W, y = (1 - bb.maxY) * H
            let w = bb.width * W, h = bb.height * H
            print("\(String(s[r]))\t\(Int(x))\t\(Int(y))\t\(Int(w))\t\(Int(h))")
        }
        idx = end
    }
}
