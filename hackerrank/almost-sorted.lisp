(defun check-sorted (arr idx)
  (do ((i idx (1+ i)))
      ((>= i (1- (length arr))) t)
      (when (> (aref arr i) (aref arr (1+ i)))
        (return))))

(defun check-reverse-case (arr idx)
  (do ((i (1+ idx) (1+ i)))
      ((>= i (1- (length arr))) (list idx i))
      (when (and (> idx 0) 
                 (< (aref arr (1+ i)) (aref arr (1- idx))))
        (return))
      (when (< (aref arr i) (aref arr (1+ i)))
        (setf (aref arr i) (aref arr idx))
        (if (and (> idx 0) (check-sorted arr i))
            (return (list idx i))
            (return)))))

(defun reverse-case (arr)
  (do ((i 0 (1+ i)))
      ((>= i (1- (length arr))) t)
      (when (> (aref arr i) (aref arr (1+ i)))
        (return (operation arr i)))))

(defun swap-case (arr)
  (do ((i 0 (1+ i))
       (c nil))
      ((>= i (1- (length arr))) t)
      (when (> (aref arr i) (aref arr (1+ i)))
        (if c
            (progn )
            (setf c i)

            ))))


(get-ans #(1 2))
(get-ans #(2 1))
(get-ans #(3 1 2))
(get-ans #(1 5 4 6))
(get-ans #(2 3 4 4 5 9 7 6 5))
(get-ans #(1 2 5 4 3 10 11 12 13 15))

