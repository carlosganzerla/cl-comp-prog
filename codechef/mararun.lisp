(defun get-prize (dd d A B C)
  (let ((marathon (/ 42 d))
        (half (/ 21 d))
        (ten (/ 10 d)))
    (cond ((>= dd marathon) C)
          ((>= dd half) B)
          ((>= dd ten) A)
          (t 0))))

(defun main () 
  (dotimes (_ (read))
    (print (get-prize (read) (read) (read) (read) (read)))))

(main)
