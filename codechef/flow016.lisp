(dotimes (_ (read))
  (let ((x (read)) (y (read)))
    (format t "~A ~A~%" (gcd x y) (lcm x y))))
