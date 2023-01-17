(defun ans (r g b k)
  (destructuring-bind (m1 m2 m3) (sort (list r g b) #'>)
    (declare (ignore m1))
    (+ k (min (1- k) m2) (min (1- k) m3))))

(defun main ()
  (dotimes (_ (read))
    (write (ans (read) (read) (read) (read)))
    (terpri)))

(main)
